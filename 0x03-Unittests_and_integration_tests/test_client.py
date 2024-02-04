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
