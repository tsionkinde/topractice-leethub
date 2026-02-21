class Solution:
    def findDuplicate(self, paths):
        content_map = {}  
        for path in paths:
            parts = path.split(" ")
            folder = parts[0]

          
            for file_info in parts[1:]:
              
                name, content = file_info.split("(")

                content = content[:-1]

          
                full_path = folder + "/" + name

                if content not in content_map:
                    content_map[content] = []

                content_map[content].append(full_path)

       
        result = []
        for file_list in content_map.values():
            if len(file_list) > 1:
                result.append(file_list)

        return result
        