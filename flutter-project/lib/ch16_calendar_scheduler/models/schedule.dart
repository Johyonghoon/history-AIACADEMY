import 'package:hive/hive.dart';

part 'schedule.g.dart';

@HiveType(typeId: 0)
class Schedule extends HiveObject {
  @HiveField(0)
  String id;
  @HiveField(1)
  String content;
  @HiveField(2)
  DateTime date; // ❸ 일정 날짜, 날짜 열
  @HiveField(3)
  int startTime; // 시작 시간
  @HiveField(4)
  int endTime; // 종료 시간

  Schedule(this.id, this.content, this.date, this.startTime, this.endTime);

  @override
  String toString() {
    return '{content: $content, date: $date, '
        'startTime: $startTime, endTime: $endTime}';
  }
}