class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # 두 놀이기구를 타는 순서(육상→수상, 수상→육상)를 각각 계산해 최솟값을 고른다. 첫 기구의 종료 시각을 정렬한 뒤 두 번째 기구를 시작 시각 순으로 훑으며 '이미 열린 기구 중 최소 소요' 또는 '아직 안 열린 기구 중 최소 종료'를 쓴다
        # 시간 복잡도: O(n log n + m log m)
        def best_after_first(first_start_time: List[int], first_duration: List[int], second_start_time: List[int], second_duration: List[int]) -> int:
            first_finish_times = sorted(start + duration for start, duration in zip(first_start_time, first_duration))
            second_rides = sorted(zip(second_start_time, second_duration))

            answer = float("inf")

            index = 0
            min_open_duration = float("inf")
            for finish_time in first_finish_times:  # 종료 시각 이전에 열린 기구는 바로 탈 수 있으므로 소요 시간이 가장 짧은 것을 고른다
                while (index < len(second_rides) and second_rides[index][0] <= finish_time):
                    min_open_duration = min(min_open_duration, second_rides[index][1])
                    index += 1

                if min_open_duration != float("inf"):
                    answer = min(answer, finish_time + min_open_duration)

            index = len(second_rides) - 1
            min_future_finish = float("inf")
            for finish_time in reversed(first_finish_times):  # 종료 시각 이후에 열리는 기구는 여는 시각에 타므로 start + duration이 가장 작은 것을 고른다
                while index >= 0 and second_rides[index][0] > finish_time:
                    start, duration = second_rides[index]
                    min_future_finish = min(min_future_finish, start + duration)
                    index -= 1

                answer = min(answer, min_future_finish)

            return answer

        return min(best_after_first(landStartTime, landDuration, waterStartTime, waterDuration), best_after_first(waterStartTime, waterDuration, landStartTime, landDuration))
