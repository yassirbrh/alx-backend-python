#!/usr/bin/env python3
'''
    Class TestGithubOrgClient that inherits from unittest.TestCase
'''
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict
import unittest
from unittest.mock import Mock, MagicMock, patch


class TestGithubOrgClient(unittest.TestCase):
    '''
        Class TestGithubOrgClient that inherits from unittest.TestCase.
    '''
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    @patch('client.get_json')
    def test_org(self, org: str, response: Dict, mock_mtd: MagicMock) -> None:
        '''
            Test method for GithubOrgClient.org
        '''
        mock_mtd.return_value = MagicMock(return_value=response)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), response)
        new_org = "https://api.github.com/orgs/{}".format(org)
        mock_mtd.assert_called_once_with(new_org)
