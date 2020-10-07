import os
from easyporouspy.metaimage.MetaImage import MetaImage
from easyporouspy.segmentation.SegmentationGeneric import SegmentationGeneric


def test_generic_segmentation():
    dir = r"../../environment_test"
    name = "seg_test"
    mim = MetaImage(name=name)
    mim.create_dir(dir=dir)
    path = r"../../environment_test/file_test"
    name_file = 'im.json'
    mim.save_im_js(name=name_file, path_file=path)
    seg_generic = SegmentationGeneric(mim)
    assert os.path.isdir(seg_generic.dir)
    assert seg_generic.dir == os.path.join(mim.mim_dir, 'segmentation')
    lim = 100
    seg_generic.threshold(lim)
    assert seg_generic.thrs == lim
    seg_generic.limiar_segmentation()
    assert os.path.isfile(seg_generic.seg_im_lim)
    im = seg_generic.open_im_js(seg_generic.seg_im_lim)
    assert im.shape == (11, 840, 840)
