import math
from typing import List, Union
import numpy as np

def deg2num(lat_deg: float, lon_deg:  float, zoom: int):
    """Convert lat,lng to xyz tile coordinates.
    reference: https://developers.planet.com/docs/planetschool/xyz-tiles-and-slippy-maps/

    Args:
        lat_deg (float): latitude in decimal degrees
        lon_deg (float): longitude in decimal degrees
        zoom (int): zoom level e.g. 19

    Returns:
        x_tile (float): x in tile coordinates at specified zoom level
        y_tile (float): y in tile coordinates at specified zoom level
    """

    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = (lon_deg + 180.0) / 360.0 * n
    ytile = (1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n
    return xtile, ytile



def num2deg(xtile: Union[float, int], ytile: Union[float, int], zoom: int):
    """convert x, y, tile coordinates to lat, lng. 
    ref: https://developers.planet.com/docs/planetschool/xyz-tiles-and-slippy-maps/

    Args:
        xtile (Union[float, int]): x position
        ytile (Union[float, int]): y position
        zoom (int): zoom level e.g. 19

    Returns:
        lat_deg (float): latitude in decimal degrees
        lng_deg (float): longitude in decimal degrees
    """
    n = 2.0 ** zoom
    lng_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return lat_deg, lng_deg



def getBboxLatLng(coords: List[List]):
    """Get bounding box for a polygon.

    Args:
        coords (List[List]): list of points (x,y) = (lng,lat) with bottom left reference (e.g. [[lng,lat], [lng,lat]])

    Returns:
        x1 (float): closest distance from left reference
        y1 (float): closest distance from top reference
        x2 (float): furthest distance from left reference
        y2 (float): furthest distance from top reference

    """    

    coords = np.array(coords)
    x1 = np.min(coords[:,0])
    y1 = np.max(coords[:,1])
    x2 = np.max(coords[:,0])
    y2 = np.min(coords[:,1])

    return x1, y1, x2, y2



def getBboxTileCoords(coords: List[List], zxy: str):
    """Get bounding box for a polygon. output is in tile coordinates

    Args:
        coords (List[List]): list of points (x,y) = (lng,lat) with bottom left reference (e.g. [[lng,lat], [lng,lat]])

    Returns:
        x1 (float): closest distance from tile left side
        y1 (float): closest distance from tile top side
        x2 (float): furthest distance from tile left side
        y2 (float): furthest distance from tile top side

    """    

    # get bounding box (top left reference)
    x1, y1, x2, y2 = getBboxLatLng(coords)

    z = int(zxy.split("/")[0])
    x = int(zxy.split("/")[1])
    y = int(zxy.split("/")[2])

    # get annotation bounding box in tile coordinates
    x1, y1 = deg2num(y1, x1, z)
    x2, y2 = deg2num(y2, x2, z)

    x1 -= x
    x2 -= x
    y1 -= y
    y2 -= y

    return x1, y1, x2, y2


def getOverlap(coords: List[List], zxy: str):
    """ Get the portion of a bounding box that is inside a tile

    Args:
        coords (List[List]): list of points in the polygon (lat,lng)
        zxy (str): tile e.g. 12/345/678

    Returns:
        float: overlap [0,1]
    """
    x1, x2, y1, y2 = getBboxTileCoords(coords, zxy)

    # get intersection area
    x_overlap = np.clip(x2, 0, 1) - np.clip(x1, 0, 1)
    y_overlap = np.clip(y2, 0, 1) - np.clip(y1, 0, 1)

    # get annotation area
    annotation_area = abs((x2-x1)*(y2-y1))
    overlap_area = (x_overlap*y_overlap) / annotation_area
    return overlap_area

    

def bboxFromCoords(coordinates: List[List], zxy: str, width: int, height: int, clip: bool = False):
    """ Get a bounding box from a polygon (lng, lat)

    Args:
        coordinates (List[List]): List of points in polygon (lng, lat)
        zxy (str): Tile zxy
        width (int): Width in pixels
        height (int): Height in pixels
        clip (Optional[bool]): Clip the boxes to the edge of the tiles

    Returns:
        x1 (int): top-left x coordinate
        y1 (int): top-left y coordinate
        x2 (int): bottom-right x coordinate
        y2 (int): bottom-right y coordinate
    """

    bbox = getBboxTileCoords(coordinates, zxy)
    
    [x1, y1, x2, y2] = bbox
    
    if clip:
        x1 = np.clip(bbox[0], 0, 1)
        y1 = np.clip(bbox[1], 0, 1)
        x2 = np.clip(bbox[2], 0, 1)
        y2 = np.clip(bbox[3], 0, 1)

    x1 *= width
    y1 *= height
    x2 *= width
    y2 *= height

    return x1, y1, x2, y2


def bboxToCoco(x1: int, y1: int, x2: int, y2: int):
    """ Convert two-point bbox to coco format

    Args:
        x1 (int): top-left x coordinate
        y1 (int): top-left y coordinate
        x2 (int): bottom-right x coordinate
        y2 (int): bottom-right y coordinate

    Returns:
        x (int): top-left x coordinate
        y (int): top-left y coordinate
        w (int): box width
        h (int): box height
    """

    w = int(x2-x1)
    h = int(y2-y1)
    
    return x1, y1, w, h

def coordsFromBbox(
        x1: int, 
        y1: int, 
        x2: int, 
        y2: int, 
        zxy: str, 
        width: int, 
        height: int) -> List[List[float]]:
    """Get lng,lat coordinate list from a bounding box and width height

    Args:
        x1 (int): left edge
        y1 (int): top edge
        x2 (int): right edge
        y2 (int): bottom edge
        zxy (str): tile e.g. 12/345/678
        width (int): tile width in pixels
        height (int): tile height in pixels


    Returns:
        List[List[float]]: coordinate for polygon

    """

    z,x,y = splitZXY(zxy)
    x1 /= width
    y1 /= height
    x2 /= width
    y2 /= height
    points = [[x+x1, y+y1],
        [x+x2, y+y1],
        [x+x2, y+y2],
        [x+x1, y+y2],
        [x+x1, y+y1]]
    points_lat_lng = []
    for point in points:
        lat, lng = num2deg(point[0], point[1], z)
        points_lat_lng.append([lng, lat])
    return points_lat_lng
    

def splitZXY(zxy: str):
    """ Split an zxy string up in to z,x,y component

    Args:
        zxy (str): zxy string e.g. 12/345/678

    Returns:
        z: tile zoom level
        x: tile x
        y: tile y

    Example:
        Consider splitting the zxy string "12/345/678"::

            z, x, y = splitZXY("12/345/678")
            print(z,x,y)
            # result: 12, 345, 678

    """

    z = int(zxy.split("/")[0])
    x = int(zxy.split("/")[1])
    y = int(zxy.split("/")[2])

    return z, x, y


def urlFromZxy(z: int, x: int, y: int, imagery_id: str, baseUrl: str) -> str:
    """Generate a url given a zxy and an imagery id

    Args:
        z (int): zoom
        x (int): x tile
        y (int): y tile
        imagery_id (str): id of the imagery
        baseUrl (str): base url e.g. https://project-kiwi.org/

    Returns:
        str: url to download the tile, however api key is still required as a param
    """    
    return f"{baseUrl}/api/get_tile/{imagery_id}/{z}/{x}/{y}"