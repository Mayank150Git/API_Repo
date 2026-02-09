from playwright.sync_api import Playwright


def test_TC1(playwright:Playwright):

    data = {"title":"QA Automation","body":"Testing POST method","userId":1}

    Session = playwright.request.new_context()
    PostResponse = Session.post("https://jsonplaceholder.typicode.com/posts",
                                data = data,
                                headers={"Content-Type": "application/json"})

    JsonResponse = PostResponse.json()
    print(JsonResponse)
    assert PostResponse.status == 200




