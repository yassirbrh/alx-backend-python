#!/usr/bin/env python3
'''
    Class TestGithubOrgClient that inherits from unittest.TestCase
'''
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import Mock, MagicMock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    '''
        Class TestGithubOrgClient that inherits from unittest.TestCase.
    '''
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch(
        'client.get_json',
    )
    def test_org(self, org: str, response: Dict, mock_mtd: MagicMock) -> None:
        '''
            test_org: function
            @self: class constructor.
            @org: the org name.
            @response: the response.
            mock_mtd: The mocked function.
            return: None
        '''
        mock_mtd.return_value = MagicMock(return_value=response)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), response)
        new_org = "https://api.github.com/orgs/{}".format(org)
        mock_mtd.assert_called_once_with(new_org)

    def test_public_repos_url(self) -> None:
        '''
            test_public_repos_url: function
            @self: class constructor.
            return: None
        '''
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mocked_org_method:
            mocked_org_method.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json: MagicMock) -> None:
        '''
            test_public_repos: function
            @self: class constructor.
            @mocked_get_json: MagicMock instance.
            return: No return.
        '''
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 460600860,
                    "node_id": "R_kgDOG3Q2HA",
                    "name": ".allstar",
                    "full_name": "google/.allstar",
                    "private": False,
                },
                {
                    "id": 170908616,
                    "node_id": "MDEwOlJlcG9zaXRvcnkxNzA5MDg2MTY=",
                    "name": ".github",
                    "full_name": "google/.github",
                    "private": False,
                }
            ]
        }
        mocked_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    ".allstar",
                    ".github",
                ],
            )
            mocked_public_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, result: bool) -> None:
        """
            test_has_licence: function
            @self: class constructor.
            @repo: repository.
            @key: key of licence.
            @result: True if it has, otherwise False
        """
        github_org_client = GithubOrgClient("google")
        client_has_licence = github_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, result)
