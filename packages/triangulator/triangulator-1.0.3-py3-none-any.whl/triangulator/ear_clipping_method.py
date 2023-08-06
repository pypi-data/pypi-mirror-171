from triangulator.geometry.angles import get_polygon_internal_angle
from triangulator.geometry.points import is_point_inside_triangle

def triangulate(poligon: tuple) -> list:
    """
    This function will triangulate any polygon and return a list of triangles

        Parameters: 
            poligon (tuple): A tuple of tuples with the points of the polygon
        Returns:
            list: A list of tuples with the triangles vertices

    """


    """
    Explanation:
    ============

        This function will triangulate any polygon and return a list of triangles
        The algorithm is based on the ear clipping method, which is a simple method

    Algorithm:
    ==========

        1. Find the internal angle of each vertex
        2. Check if the angle is less than 180 degrees, skip if not
        3. Check if there are any polygon points inside the triangle formed by the vertex and its neighbors
        4. If there are no points inside the triangle, then the vertex is an ear
        5. If the vertex is an ear, add the triangle to the list of triangles
        6. Remove the ear and repeat the process until there are no more ears

    References:
    ===========
        https://en.wikipedia.org/wiki/Polygon_triangulation#Ear_clipping_method
        https://www.youtube.com/watch?v=QAdfkylpYwc
    """

    final_triangles = []
    vertices = list(poligon)
    original_vertices = list(poligon)
    triangles_finded = -1
    
    # While there are triangles to be found
    while(triangles_finded != 0): 
      triangles_finded = 0

      for index, _ in enumerate(vertices):
        prev_vertice = vertices[index - 1]
        next_vertice = vertices[(index + 1) % (len(vertices))] # using mod to avoid index out of range
        vertice = vertices[index]

        # Get Vector from prev_vertice to vertice
        vector1 = (vertice[0] - prev_vertice[0], vertice[1] - prev_vertice[1])
        # Get Vector from vertice to next_vertice
        vector2 = (next_vertice[0] - vertice[0], next_vertice[1] - vertice[1])
        # Get internal angle
        angle = get_polygon_internal_angle(vector1, vector2)

        if angle >= 180:
            # Skip because angle is greater than 180
            continue
        else:
            # Build a triangle with the three vertices
            triangle = (prev_vertice, vertice, next_vertice)
            # Get vertices that are not part of the triangle
            points = [p for p in original_vertices if p not in triangle]
            # Check if there is a vertice inside the triangle
            inside_evaluation = [is_point_inside_triangle(triangle, point) for point in points]
            # If are not points inside the triangle
            if True in inside_evaluation:
                # Skip because point is inside triangle
                continue
            else:
                # Add triangle to final triangles
                final_triangles.append(triangle)
                # Remove vertice from vertices
                vertices.pop(index)
                # Increment triangles finded
                triangles_finded += 1
                break
    return final_triangles
