class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for car in cars:
            time_to_target = (target - car[0]) / car[1]
            if stack:
                if time_to_target > stack[-1]:
                    stack.append(time_to_target)
                else:
                    continue
            else:
                stack.append(time_to_target)
        return len(stack)
