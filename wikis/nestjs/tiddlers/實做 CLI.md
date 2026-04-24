使用獨立應用程式 (Standalone applications) 模式來實做客製化 CLI：

```typescript
async function bootstrap() {
  const app = await NestFactory.createApplicationContext(AppModule);
  // your application logic here ...
}
bootstrap();
```