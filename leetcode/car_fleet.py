class Solution:
    
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        sorted_positions = sorted(
            zip(position, speed), 
            reverse=True
        )
        
        count = 0
        current_arrival = 0
        
        for p, s in sorted_positions:
            arrival = (target - p) / s
            
            if arrival <= current_arrival:
                continue
            
            count += 1
            current_arrival = arrival
            
        return count
    
if __name__ == "__main__":
    print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))