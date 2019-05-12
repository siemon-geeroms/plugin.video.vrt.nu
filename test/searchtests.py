# -*- coding: utf-8 -*-

# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, unicode_literals
import mock
import unittest

from resources.lib.vrtplayer import vrtapihelper


class TestVRTPlayer(unittest.TestCase):

    _kodiwrapper = mock.MagicMock()
    _kodiwrapper.get_proxies = mock.MagicMock(return_value=dict())
    _kodiwrapper.get_localized_dateshort = mock.MagicMock(return_value='%d-%m-%Y')
    _apihelper = vrtapihelper.VRTApiHelper(_kodiwrapper)

    def test_search_journaal(self):
        ''' Test for journaal '''
        search_items, sort, ascending = self._apihelper.search('journaal', page=1)

        # Test we get a non-empty search result
        self.assertEqual(len(search_items), 50)
        self.assertEqual(sort, 'dateadded')
        self.assertFalse(ascending)

    def test_search_journaal_page2(self):
        ''' Test for journaal '''
        search_items, sort, ascending = self._apihelper.search('journaal', page=2)

        # Test we get a non-empty search result
        self.assertEqual(len(search_items), 50)
        self.assertEqual(sort, 'dateadded')
        self.assertFalse(ascending)

    def test_search_weer(self):
        ''' Test for journaal '''
        search_items, sort, ascending = self._apihelper.search('weer', page=1)

        # Test we get a non-empty search result
        self.assertEqual(len(search_items), 50)
        self.assertEqual(sort, 'dateadded')
        self.assertFalse(ascending)


if __name__ == '__main__':
    unittest.main()