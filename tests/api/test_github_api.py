import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


# @pytest.mark.api
# def test_repo_can_be_found(github_api):
#    r = github_api.search_repo("become-qa-auto")
#    assert r["total_count"] == 58
#    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Індивідуальна частина проєктного завдання №4


owner = "OksanaPavlenko1"
owner = owner.lower()
repo = "OksanaQAauto"
repolower = repo.lower()
ref = "a127aaa5da5974f4a1f51c9bc03909e24327f097"


@pytest.mark.api
def test_owner_can_be_found(github_api):
    r = github_api.get_commit(owner, repo, ref)
    assert r["author"]["login"] == "OksanaPavlenko1"


@pytest.mark.api
def test_owner_cannot_be_found(github_api):
    r = github_api.get_commit("OksanaPavlenko2", repo, ref)
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_name_lower(github_api):
    r = github_api.get_commit(owner, repolower, ref)
    assert r["author"]["login"] == "OksanaPavlenko1"


@pytest.mark.api
def test_repo_name_with_extention(github_api):
    r = github_api.get_commit(owner, "OksanaQAauto.git", ref)
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_branch_name(github_api):
    r = github_api.get_branch(owner, repo, "main")
    assert r["name"] == "main"


@pytest.mark.api
def test_branch_name_vildcard_character(github_api):
    r = github_api.get_branch(owner, repo, "main*")
    assert r["message"] == "Branch not found"
