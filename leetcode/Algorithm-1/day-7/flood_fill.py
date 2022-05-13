class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        image_width_last_index = len(image[0]) - 1
        image_height_last_index = len(image) - 1
        print(image_width_last_index)
        print(image_height_last_index)

        old_value = image[int(sr)][int(sc)]
        queue = []
        queue.append((sr, sc))
        visited = set()

        while queue:
            (r, c) = queue[0]
            queue.pop(0)

            if (r, c) not in visited:

                image[r][c] = newColor
                visited.add((r, c))

                if c > 0 and image[r][c - 1] == old_value:
                    queue.append((r, c - 1))
                elif r > 0 and image[r - 1][c] == old_value:
                    queue.append((r - 1, c))
                elif r < image_height_last_index and image[r + 1][c] == old_value:
                    queue.append((r + 1, c))
                elif c < image_width_last_index and image[r][c + 1] == old_value:
                    queue.append((r, c + 1))
        print(image)
        return image


s = Solution()
s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2)
