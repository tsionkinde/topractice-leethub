class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    
        count_map = {}

        for item in cpdomains:
            count_str, domain = item.split()
            count = int(count_str)

            parts = domain.split(".")

        
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])

                if subdomain not in count_map:
                    count_map[subdomain] = 0

                count_map[subdomain] += count

     
        result = []
        for domain, total in count_map.items():
            result.append(str(total) + " " + domain)

        return result
        