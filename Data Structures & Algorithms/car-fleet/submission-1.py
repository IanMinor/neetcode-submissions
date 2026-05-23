class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for pos, speed in cars:
            time_to_target = (target - pos) / speed

            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
        return len(stack)
