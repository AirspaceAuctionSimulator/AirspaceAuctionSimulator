import unittest

from Simulator import Coordinate2D, Coordinate3D, Coordinate4D


class CoordinatesTest(unittest.TestCase):
    def test_2D(self):
        aa = Coordinate2D(20, 42)
        self.assertDictEqual(aa.to_dict(), {"x": 20, "z": 42})
        self.assertEqual("( 20.00,  42.00)", str(aa))
        bb = Coordinate2D(20, 42)
        self.assertEqual(aa, bb)
        cc = Coordinate2D(20, 43)
        self.assertNotEqual(cc, aa)
        dd = Coordinate2D(40, 85)
        self.assertEqual(aa + cc, dd)
        self.assertNotEqual(aa + dd, cc)
        self.assertEqual(dd - cc, aa)
        self.assertNotEqual(dd - cc, dd)
        self.assertEqual(62, aa.l1)
        self.assertAlmostEqual(46.5188134, aa.l2, 3)
        self.assertEqual(1, aa.distance(cc))
        self.assertEqual(1, aa.distance(cc, l2=True))
        self.assertEqual(aa, aa.clone())
        self.assertNotEqual(id(aa), id(aa.clone()))

    def test_3D(self):
        aa = Coordinate3D(25, 12, 22)
        self.assertDictEqual(aa.to_dict(), {"x": 25, "y": 12, "z": 22})
        self.assertEqual("( 25.00,  12.00,  22.00)", str(aa), )
        bb = Coordinate3D(25, 12, 22)
        self.assertEqual(aa, bb)
        cc = Coordinate3D(25, 11, 22)
        self.assertNotEqual(aa, cc)
        dd = Coordinate3D(50, 23, 44)
        self.assertEqual(aa + cc, dd)
        self.assertNotEqual(aa + dd, cc)
        self.assertEqual(dd - cc, aa)
        self.assertNotEqual(dd - cc, dd)
        self.assertEqual(59, aa.l1)
        self.assertAlmostEqual(35.39774004, aa.l2, 3)
        self.assertEqual(1, aa.distance(cc))
        self.assertEqual(1, aa.distance(cc, l2=True))
        self.assertEqual(aa, aa.clone())
        self.assertNotEqual(id(aa), id(aa.clone()))

    def test_4D(self):
        aa = Coordinate4D(21, 1, 19, 8)
        self.assertDictEqual(aa.to_dict(), {"x": 21, "y": 1, "z": 19, "t": 8})
        self.assertEqual(str(aa), "( 21,   1,  19,   8)")
        bb = Coordinate4D(21, 1, 19, 8)
        self.assertEqual(aa, bb)
        cc = Coordinate4D(21, 1, 19, 9)
        self.assertNotEqual(aa, cc)
        dd = Coordinate4D(42, 2, 38, 17)
        self.assertEqual(aa + cc, dd)
        self.assertNotEqual(aa + dd, cc)
        self.assertEqual(dd - cc, aa)
        self.assertNotEqual(dd - cc, dd)
        self.assertEqual(49., aa.l1)
        self.assertAlmostEqual(29.44486373, aa.l2, 3)
        self.assertEqual(0, aa.distance(cc))
        ee = Coordinate3D(1, 2, 3)
        self.assertEqual(37, aa.distance(ee))
        self.assertEqual(0, aa.distance(cc, l2=True))
        self.assertEqual(aa, aa.clone())
        self.assertNotEqual(id(aa), id(aa.clone()))
        ff = Coordinate3D(21, 1, 19)
        self.assertEqual(Coordinate4D.from_3D(ff, 8), aa)
        self.assertEqual(ff, aa.to_3D())
        self.assertListEqual(aa.list_rep(), [21, 1, 19, 8])
        self.assertListEqual(aa.tree_query_cube_rep(2, 4), [19, -1, 17, 8, 23, 3, 21, 12])
        self.assertEqual(aa.distance(cc), 0)
