## 問題

資料在 ECS 架構中，只有在引擎的 tick 週期內可以被訪問，方法的執行亦然；而在 OOP 架構中，則是可以透過指標或參考在任意時機直接訪問成員或呼叫方法。

重構過程必然會面臨兩種架構同時存在的問題，如何處理「將部份邏輯移至 ECS 架構，同時保持向下兼容不破壞仍留在 OOP 架構下實作的邏輯」變成一個大問題。

## 解決方案

透過類似以下的程式：

```typescript
@injectable()
export class SkyAdaptor implements ISystem, SkyProvider {
    private threePosition: Vector3 | null = null;
    private threeCsm: CSM | null = null;

    constructor(
        @inject('Store')
        @named('store')
        private store: Store<Entity>,
        @inject('SceneProvider')
        private sceneProvider: ISceneProvider,
        @inject('CameraProvider')
        private cameraProvider: ICameraProvider,
    ) {
    }
    public init(): Promise<void> | void {
        //...

        this.threePosition = threePosition;
        this.threeCsm = threeCsm;
    }
    public preload(): Promise<void> | void {/** Not Behavior */ }
    public create(): Promise<void> | void {/** Not Behavior */ }
    public update(time: number, delta: number): void {
        //...
    }
    public dispose(): Promise<void> | void {/** Not Behavior */ }

    public get sunPosition(): Vector3 {
        if (this.threePosition) {
            return this.threePosition;
        }
        throw new Error('The system is not initialize or already disposed.');
    }
    public get csm(): CSM {
        if (this.threeCsm) {
            return this.threeCsm
        }
        throw new Error('The system is not initialize or already disposed.');
    }
}
```

IoC 設定：

```typescript
container.bind<SkyAdaptor>('SkyAdaptor').to(SkyAdaptor).inSingletonScope();
container.bind<ICameraProvider>('SkyProvider').toService('SkyAdaptor');
container.bind<ISystem>('System').toService('SkyProvider');
```

如此一來一個 Adaptor 實例將同時作為 ECS 的 System 以及 OOP 的某個嵌容界面作用，並且將實例化與注入之類的複雜工作交由 IoC 處理。

該策略本質上是一種[絞殺者模式](#絞殺者模式)。