# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.15.0-rc3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.repository_api import RepositoryApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRepositoryApi(unittest.TestCase):
    """RepositoryApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.repository_api.RepositoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_current_user_repo(self):
        """Test case for create_current_user_repo

        Create a repository  # noqa: E501
        """
        pass

    def test_create_fork(self):
        """Test case for create_fork

        Fork a repository  # noqa: E501
        """
        pass

    def test_generate_repo(self):
        """Test case for generate_repo

        Create a repository using a template  # noqa: E501
        """
        pass

    def test_get_annotated_tag(self):
        """Test case for get_annotated_tag

        Gets the tag object of an annotated tag (not lightweight tags)  # noqa: E501
        """
        pass

    def test_get_blob(self):
        """Test case for get_blob

        Gets the blob of a repository.  # noqa: E501
        """
        pass

    def test_get_tree(self):
        """Test case for get_tree

        Gets the tree of a repository.  # noqa: E501
        """
        pass

    def test_list_forks(self):
        """Test case for list_forks

        List a repository's forks  # noqa: E501
        """
        pass

    def test_repo_add_collaborator(self):
        """Test case for repo_add_collaborator

        Add a collaborator to a repository  # noqa: E501
        """
        pass

    def test_repo_add_team(self):
        """Test case for repo_add_team

        Add a team to a repository  # noqa: E501
        """
        pass

    def test_repo_add_topc(self):
        """Test case for repo_add_topc

        Add a topic to a repository  # noqa: E501
        """
        pass

    def test_repo_check_collaborator(self):
        """Test case for repo_check_collaborator

        Check if a user is a collaborator of a repository  # noqa: E501
        """
        pass

    def test_repo_check_team(self):
        """Test case for repo_check_team

        Check if a team is assigned to a repository  # noqa: E501
        """
        pass

    def test_repo_create_branch(self):
        """Test case for repo_create_branch

        Create a branch  # noqa: E501
        """
        pass

    def test_repo_create_branch_protection(self):
        """Test case for repo_create_branch_protection

        Create a branch protections for a repository  # noqa: E501
        """
        pass

    def test_repo_create_file(self):
        """Test case for repo_create_file

        Create a file in a repository  # noqa: E501
        """
        pass

    def test_repo_create_hook(self):
        """Test case for repo_create_hook

        Create a hook  # noqa: E501
        """
        pass

    def test_repo_create_key(self):
        """Test case for repo_create_key

        Add a key to a repository  # noqa: E501
        """
        pass

    def test_repo_create_pull_request(self):
        """Test case for repo_create_pull_request

        Create a pull request  # noqa: E501
        """
        pass

    def test_repo_create_pull_review(self):
        """Test case for repo_create_pull_review

        Create a review to an pull request  # noqa: E501
        """
        pass

    def test_repo_create_pull_review_requests(self):
        """Test case for repo_create_pull_review_requests

        create review requests for a pull request  # noqa: E501
        """
        pass

    def test_repo_create_release(self):
        """Test case for repo_create_release

        Create a release  # noqa: E501
        """
        pass

    def test_repo_create_release_attachment(self):
        """Test case for repo_create_release_attachment

        Create a release attachment  # noqa: E501
        """
        pass

    def test_repo_create_status(self):
        """Test case for repo_create_status

        Create a commit status  # noqa: E501
        """
        pass

    def test_repo_create_tag(self):
        """Test case for repo_create_tag

        Create a new git tag in a repository  # noqa: E501
        """
        pass

    def test_repo_delete(self):
        """Test case for repo_delete

        Delete a repository  # noqa: E501
        """
        pass

    def test_repo_delete_branch(self):
        """Test case for repo_delete_branch

        Delete a specific branch from a repository  # noqa: E501
        """
        pass

    def test_repo_delete_branch_protection(self):
        """Test case for repo_delete_branch_protection

        Delete a specific branch protection for the repository  # noqa: E501
        """
        pass

    def test_repo_delete_collaborator(self):
        """Test case for repo_delete_collaborator

        Delete a collaborator from a repository  # noqa: E501
        """
        pass

    def test_repo_delete_file(self):
        """Test case for repo_delete_file

        Delete a file in a repository  # noqa: E501
        """
        pass

    def test_repo_delete_git_hook(self):
        """Test case for repo_delete_git_hook

        Delete a Git hook in a repository  # noqa: E501
        """
        pass

    def test_repo_delete_hook(self):
        """Test case for repo_delete_hook

        Delete a hook in a repository  # noqa: E501
        """
        pass

    def test_repo_delete_key(self):
        """Test case for repo_delete_key

        Delete a key from a repository  # noqa: E501
        """
        pass

    def test_repo_delete_pull_review(self):
        """Test case for repo_delete_pull_review

        Delete a specific review from a pull request  # noqa: E501
        """
        pass

    def test_repo_delete_pull_review_requests(self):
        """Test case for repo_delete_pull_review_requests

        cancel review requests for a pull request  # noqa: E501
        """
        pass

    def test_repo_delete_release(self):
        """Test case for repo_delete_release

        Delete a release  # noqa: E501
        """
        pass

    def test_repo_delete_release_attachment(self):
        """Test case for repo_delete_release_attachment

        Delete a release attachment  # noqa: E501
        """
        pass

    def test_repo_delete_release_by_tag(self):
        """Test case for repo_delete_release_by_tag

        Delete a release by tag name  # noqa: E501
        """
        pass

    def test_repo_delete_tag(self):
        """Test case for repo_delete_tag

        Delete a repository's tag by name  # noqa: E501
        """
        pass

    def test_repo_delete_team(self):
        """Test case for repo_delete_team

        Delete a team from a repository  # noqa: E501
        """
        pass

    def test_repo_delete_topic(self):
        """Test case for repo_delete_topic

        Delete a topic from a repository  # noqa: E501
        """
        pass

    def test_repo_dismiss_pull_review(self):
        """Test case for repo_dismiss_pull_review

        Dismiss a review for a pull request  # noqa: E501
        """
        pass

    def test_repo_download_pull_diff(self):
        """Test case for repo_download_pull_diff

        Get a pull request diff  # noqa: E501
        """
        pass

    def test_repo_download_pull_patch(self):
        """Test case for repo_download_pull_patch

        Get a pull request patch file  # noqa: E501
        """
        pass

    def test_repo_edit(self):
        """Test case for repo_edit

        Edit a repository's properties. Only fields that are set will be changed.  # noqa: E501
        """
        pass

    def test_repo_edit_branch_protection(self):
        """Test case for repo_edit_branch_protection

        Edit a branch protections for a repository. Only fields that are set will be changed  # noqa: E501
        """
        pass

    def test_repo_edit_git_hook(self):
        """Test case for repo_edit_git_hook

        Edit a Git hook in a repository  # noqa: E501
        """
        pass

    def test_repo_edit_hook(self):
        """Test case for repo_edit_hook

        Edit a hook in a repository  # noqa: E501
        """
        pass

    def test_repo_edit_pull_request(self):
        """Test case for repo_edit_pull_request

        Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.  # noqa: E501
        """
        pass

    def test_repo_edit_release(self):
        """Test case for repo_edit_release

        Update a release  # noqa: E501
        """
        pass

    def test_repo_edit_release_attachment(self):
        """Test case for repo_edit_release_attachment

        Edit a release attachment  # noqa: E501
        """
        pass

    def test_repo_get(self):
        """Test case for repo_get

        Get a repository  # noqa: E501
        """
        pass

    def test_repo_get_all_commits(self):
        """Test case for repo_get_all_commits

        Get a list of all commits from a repository  # noqa: E501
        """
        pass

    def test_repo_get_archive(self):
        """Test case for repo_get_archive

        Get an archive of a repository  # noqa: E501
        """
        pass

    def test_repo_get_assignees(self):
        """Test case for repo_get_assignees

        Return all users that have write access and can be assigned to issues  # noqa: E501
        """
        pass

    def test_repo_get_branch(self):
        """Test case for repo_get_branch

        Retrieve a specific branch from a repository, including its effective branch protection  # noqa: E501
        """
        pass

    def test_repo_get_branch_protection(self):
        """Test case for repo_get_branch_protection

        Get a specific branch protection for the repository  # noqa: E501
        """
        pass

    def test_repo_get_by_id(self):
        """Test case for repo_get_by_id

        Get a repository by id  # noqa: E501
        """
        pass

    def test_repo_get_combined_status_by_ref(self):
        """Test case for repo_get_combined_status_by_ref

        Get a commit's combined status, by branch/tag/commit reference  # noqa: E501
        """
        pass

    def test_repo_get_contents(self):
        """Test case for repo_get_contents

        Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir  # noqa: E501
        """
        pass

    def test_repo_get_contents_list(self):
        """Test case for repo_get_contents_list

        Gets the metadata of all the entries of the root dir  # noqa: E501
        """
        pass

    def test_repo_get_editor_config(self):
        """Test case for repo_get_editor_config

        Get the EditorConfig definitions of a file in a repository  # noqa: E501
        """
        pass

    def test_repo_get_git_hook(self):
        """Test case for repo_get_git_hook

        Get a Git hook  # noqa: E501
        """
        pass

    def test_repo_get_hook(self):
        """Test case for repo_get_hook

        Get a hook  # noqa: E501
        """
        pass

    def test_repo_get_issue_templates(self):
        """Test case for repo_get_issue_templates

        Get available issue templates for a repository  # noqa: E501
        """
        pass

    def test_repo_get_key(self):
        """Test case for repo_get_key

        Get a repository's key by id  # noqa: E501
        """
        pass

    def test_repo_get_languages(self):
        """Test case for repo_get_languages

        Get languages and number of bytes of code written  # noqa: E501
        """
        pass

    def test_repo_get_pull_request(self):
        """Test case for repo_get_pull_request

        Get a pull request  # noqa: E501
        """
        pass

    def test_repo_get_pull_request_commits(self):
        """Test case for repo_get_pull_request_commits

        Get commits for a pull request  # noqa: E501
        """
        pass

    def test_repo_get_pull_review(self):
        """Test case for repo_get_pull_review

        Get a specific review for a pull request  # noqa: E501
        """
        pass

    def test_repo_get_pull_review_comments(self):
        """Test case for repo_get_pull_review_comments

        Get a specific review for a pull request  # noqa: E501
        """
        pass

    def test_repo_get_raw_file(self):
        """Test case for repo_get_raw_file

        Get a file from a repository  # noqa: E501
        """
        pass

    def test_repo_get_release(self):
        """Test case for repo_get_release

        Get a release  # noqa: E501
        """
        pass

    def test_repo_get_release_attachment(self):
        """Test case for repo_get_release_attachment

        Get a release attachment  # noqa: E501
        """
        pass

    def test_repo_get_release_by_tag(self):
        """Test case for repo_get_release_by_tag

        Get a release by tag name  # noqa: E501
        """
        pass

    def test_repo_get_reviewers(self):
        """Test case for repo_get_reviewers

        Return all users that can be requested to review in this repo  # noqa: E501
        """
        pass

    def test_repo_get_single_commit(self):
        """Test case for repo_get_single_commit

        Get a single commit from a repository  # noqa: E501
        """
        pass

    def test_repo_get_tag(self):
        """Test case for repo_get_tag

        Get the tag of a repository by tag name  # noqa: E501
        """
        pass

    def test_repo_list_all_git_refs(self):
        """Test case for repo_list_all_git_refs

        Get specified ref or filtered repository's refs  # noqa: E501
        """
        pass

    def test_repo_list_branch_protection(self):
        """Test case for repo_list_branch_protection

        List branch protections for a repository  # noqa: E501
        """
        pass

    def test_repo_list_branches(self):
        """Test case for repo_list_branches

        List a repository's branches  # noqa: E501
        """
        pass

    def test_repo_list_collaborators(self):
        """Test case for repo_list_collaborators

        List a repository's collaborators  # noqa: E501
        """
        pass

    def test_repo_list_git_hooks(self):
        """Test case for repo_list_git_hooks

        List the Git hooks in a repository  # noqa: E501
        """
        pass

    def test_repo_list_git_refs(self):
        """Test case for repo_list_git_refs

        Get specified ref or filtered repository's refs  # noqa: E501
        """
        pass

    def test_repo_list_hooks(self):
        """Test case for repo_list_hooks

        List the hooks in a repository  # noqa: E501
        """
        pass

    def test_repo_list_keys(self):
        """Test case for repo_list_keys

        List a repository's keys  # noqa: E501
        """
        pass

    def test_repo_list_pull_requests(self):
        """Test case for repo_list_pull_requests

        List a repo's pull requests  # noqa: E501
        """
        pass

    def test_repo_list_pull_reviews(self):
        """Test case for repo_list_pull_reviews

        List all reviews for a pull request  # noqa: E501
        """
        pass

    def test_repo_list_release_attachments(self):
        """Test case for repo_list_release_attachments

        List release's attachments  # noqa: E501
        """
        pass

    def test_repo_list_releases(self):
        """Test case for repo_list_releases

        List a repo's releases  # noqa: E501
        """
        pass

    def test_repo_list_stargazers(self):
        """Test case for repo_list_stargazers

        List a repo's stargazers  # noqa: E501
        """
        pass

    def test_repo_list_statuses(self):
        """Test case for repo_list_statuses

        Get a commit's statuses  # noqa: E501
        """
        pass

    def test_repo_list_statuses_by_ref(self):
        """Test case for repo_list_statuses_by_ref

        Get a commit's statuses, by branch/tag/commit reference  # noqa: E501
        """
        pass

    def test_repo_list_subscribers(self):
        """Test case for repo_list_subscribers

        List a repo's watchers  # noqa: E501
        """
        pass

    def test_repo_list_tags(self):
        """Test case for repo_list_tags

        List a repository's tags  # noqa: E501
        """
        pass

    def test_repo_list_teams(self):
        """Test case for repo_list_teams

        List a repository's teams  # noqa: E501
        """
        pass

    def test_repo_list_topics(self):
        """Test case for repo_list_topics

        Get list of topics that a repository has  # noqa: E501
        """
        pass

    def test_repo_merge_pull_request(self):
        """Test case for repo_merge_pull_request

        Merge a pull request  # noqa: E501
        """
        pass

    def test_repo_migrate(self):
        """Test case for repo_migrate

        Migrate a remote git repository  # noqa: E501
        """
        pass

    def test_repo_mirror_sync(self):
        """Test case for repo_mirror_sync

        Sync a mirrored repository  # noqa: E501
        """
        pass

    def test_repo_pull_request_is_merged(self):
        """Test case for repo_pull_request_is_merged

        Check if a pull request has been merged  # noqa: E501
        """
        pass

    def test_repo_search(self):
        """Test case for repo_search

        Search for repositories  # noqa: E501
        """
        pass

    def test_repo_signing_key(self):
        """Test case for repo_signing_key

        Get signing-key.gpg for given repository  # noqa: E501
        """
        pass

    def test_repo_submit_pull_review(self):
        """Test case for repo_submit_pull_review

        Submit a pending review to an pull request  # noqa: E501
        """
        pass

    def test_repo_test_hook(self):
        """Test case for repo_test_hook

        Test a push webhook  # noqa: E501
        """
        pass

    def test_repo_tracked_times(self):
        """Test case for repo_tracked_times

        List a repo's tracked times  # noqa: E501
        """
        pass

    def test_repo_transfer(self):
        """Test case for repo_transfer

        Transfer a repo ownership  # noqa: E501
        """
        pass

    def test_repo_un_dismiss_pull_review(self):
        """Test case for repo_un_dismiss_pull_review

        Cancel to dismiss a review for a pull request  # noqa: E501
        """
        pass

    def test_repo_update_file(self):
        """Test case for repo_update_file

        Update a file in a repository  # noqa: E501
        """
        pass

    def test_repo_update_pull_request(self):
        """Test case for repo_update_pull_request

        Merge PR's baseBranch into headBranch  # noqa: E501
        """
        pass

    def test_repo_update_topics(self):
        """Test case for repo_update_topics

        Replace list of topics for a repository  # noqa: E501
        """
        pass

    def test_topic_search(self):
        """Test case for topic_search

        search topics via keyword  # noqa: E501
        """
        pass

    def test_user_current_check_subscription(self):
        """Test case for user_current_check_subscription

        Check if the current user is watching a repo  # noqa: E501
        """
        pass

    def test_user_current_delete_subscription(self):
        """Test case for user_current_delete_subscription

        Unwatch a repo  # noqa: E501
        """
        pass

    def test_user_current_put_subscription(self):
        """Test case for user_current_put_subscription

        Watch a repo  # noqa: E501
        """
        pass

    def test_user_tracked_times(self):
        """Test case for user_tracked_times

        List a user's tracked times in a repo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
