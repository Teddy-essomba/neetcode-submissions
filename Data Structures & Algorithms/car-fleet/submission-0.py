class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))

        # Sort by position descending (closest to target first)
        cars.sort(reverse=True)

        fleets = 0
        last_time = 0

        for _, time in cars:
            # If this car takes longer than the fleet ahead,
            # it forms a new fleet
            if time > last_time:
                fleets += 1
                last_time = time

        return fleets
       

        
        