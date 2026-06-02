class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def best_after_first(first_start_time: List[int], first_duration: List[int], second_start_time: List[int], second_duration: List[int]) -> int:
            first_finish_times = sorted(start + duration for start, duration in zip(first_start_time, first_duration))
            second_rides = sorted(zip(second_start_time, second_duration))

            answer = float("inf")

            index = 0
            min_open_duration = float("inf")
            for finish_time in first_finish_times:
                while (index < len(second_rides) and second_rides[index][0] <= finish_time):
                    min_open_duration = min(min_open_duration, second_rides[index][1])
                    index += 1

                if min_open_duration != float("inf"):
                    answer = min(answer, finish_time + min_open_duration)

            index = len(second_rides) - 1
            min_future_finish = float("inf")
            for finish_time in reversed(first_finish_times):
                while index >= 0 and second_rides[index][0] > finish_time:
                    start, duration = second_rides[index]
                    min_future_finish = min(min_future_finish, start + duration)
                    index -= 1

                answer = min(answer, min_future_finish)

            return answer

        return min(best_after_first(landStartTime, landDuration, waterStartTime, waterDuration), best_after_first(waterStartTime, waterDuration, landStartTime, landDuration))
