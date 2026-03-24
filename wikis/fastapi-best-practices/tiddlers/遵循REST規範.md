
開發RESTful API可以更輕鬆地在如下路由中復用依賴項：

1. `GET /courses/:course_id`
2. `GET /courses/:course_id/chapters/:chapter_id/lessons`
3. `GET /chapters/:chapter_id`

唯一需要注意的是必須在路徑中使用相同的變數名：

- 如果你有兩個端點`GET /profiles/:profile_id`和`GET /creators/:creator_id`，它們都驗證給定的`profile_id`是否存在，但`GET /creators/:creator_id`還檢查該個人資料是否是創作者，那麼最好將`creator_id`路徑變數重新命名為`profile_id`並連結這兩個依賴項。

```python
# src.profiles.dependencies
async def valid_profile_id(profile_id: UUID4) -> Mapping:
    profile = await service.get_by_id(profile_id)
    if not profile:
        raise ProfileNotFound()

    return profile

# src.creators.dependencies
async def valid_creator_id(profile: Mapping = Depends(valid_profile_id)) -> Mapping:
    if not profile["is_creator"]:
       raise ProfileNotCreator()

    return profile

# src.profiles.router.py
@router.get("/profiles/{profile_id}", response_model=ProfileResponse)
async def get_user_profile_by_id(profile: Mapping = Depends(valid_profile_id)):
    """Get profile by id."""
    return profile

# src.creators.router.py
@router.get("/creators/{profile_id}", response_model=ProfileResponse)
async def get_user_profile_by_id(
     creator_profile: Mapping = Depends(valid_creator_id)
):
    """Get creator's profile by id."""
    return creator_profile

```
