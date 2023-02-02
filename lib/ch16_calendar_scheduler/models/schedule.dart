import 'package:hive/hive.dart';

part 'schedule.g.dart';

@HiveType(typeId: 0)
class Schedules {
  @HiveField(0)
  int id;
  @HiveField(1)
  String content;
  @HiveField(2)
  DateTime date;  // ❸ 일정 날짜, 날짜 열
  @HiveField(3)
  int startTime;   // 시작 시간
  @HiveField(4)
  int endTime;     // 종료 시간

  Schedules(this.id, this.content, this.date, this.startTime, this.endTime);
}