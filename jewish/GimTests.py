import unittest
import gim

class TestGim(unittest.TestCase):

    def test_under_10(self):
        results = ('', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י')
        for i in range(1,11):
            with self.subTest(num=i):
                self.assertEqual(gim.toGStr(i), results[i])

    def test_edge_points(self):
        num_result = [ (99   , 'צט'),
                       (100  , 'ק'),
                       (999  , 'תתקצט'),
                       (1000 , 'א\''),
                       (5776 , 'ה\'תשעו'),
                     ]

        for n,r in num_result:
            with self.subTest(num=n, res=r):
                self.assertEqual(gim.toGStr(n), r)


if __name__ == "__main__":
    unittest.main()
