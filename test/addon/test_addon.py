from test.addon import client


def test_addon_manifest(client):
    response = client.get("/manifest.json")
    print(str(response))
