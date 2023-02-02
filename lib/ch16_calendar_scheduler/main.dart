import 'package:flutter/material.dart';
import 'package:flutterproject/ch16_calendar_scheduler/models/schedule.dart';
import 'package:flutterproject/ch16_calendar_scheduler/screens/table_calendar.dart';
import 'package:intl/date_symbol_data_local.dart';
import 'package:hive_flutter/hive_flutter.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await initializeDateFormatting();
  await Hive.initFlutter();
  // Adapter 등록하기
  Hive.registerAdapter<Schedules>(SchedulesAdapter());
  final schedules = await Hive.openBox<Schedules>('schedules');
  runApp(
    const MaterialApp(
      home: TableCalendar(),
    ),
  );
}
