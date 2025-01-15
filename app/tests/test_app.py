async def test_testing(setup_login):
    t: dict = await setup_login
    assert t["client"] is not None
