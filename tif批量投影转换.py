# coding=utf-8
import arcpy
env_path = str(raw_input('please input the path you store your tif files\n===>>>'))  # 输入tif文件存放路径
arcpy.env.workspace = env_path           # tif文件存放路径
rasters = arcpy.ListRasters("*", "tif")  # 获取所有以tif结尾的文件
# ===================================================================================
# 给定参考样式获取参考样式的坐标系
dsc_path = str(raw_input('please input the path you store your coordinates reference files\n===>>>'))  # 参考文件路径
# dsc = arcpy.Describe('G:\\福建_20220530\\fujian_base_WGS\\fujian.shp')  # 作为参考的文件
dsc = arcpy.Describe(dsc_path)  # 作为参考的文件
coord_sys = dsc.spatialReference   # 获取作为参考的文件的投影坐标
# inf = 'G:\\maxent_data\\pop-density\\Anhui_den2010.tif'
# cellsize = "{0} {1}".format(arcpy.Describe(inf).meanCellWidth, arcpy.Describe(inf).meanCellHeight)  # 获取栅格大小
print coord_sys
# print cellsize
# ===================================================================================
for raster in rasters:
    dsc_in = arcpy.Describe(raster)
    coord_sys_in = dsc_in.spatialReference
    out_path = r'G:\A_Hainan_20220321\NDVI_1\{}'.format(raster.encode('utf-8'))
    try:
        # ProjectRaster_management(in_raster, out_raster, out_coor_system, {resampling_type}, {cell_size},
        # {geographic_transform}, {Registration_Point}, {in_coor_system})
        arcpy.ProjectRaster_management(raster, out_path, coord_sys, "#", '0.0083100053481489', "#", "#", coord_sys_in)   #  coord_sys_in
                                                                      # 0.0089831528约为1km
        print (arcpy.GetMessages(0))                                  # 0.0083100053481489
    except arcpy.ExecuteError:
        print (arcpy.GetMessages(2))

    except Exception as ex:
        print (ex.args[0])




