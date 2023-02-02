import 'package:flutter/material.dart';
import 'package:flutterproject/ch16_calendar_scheduler/models/schedule.dart';
import 'package:flutterproject/ch16_calendar_scheduler/screens/table_calendar.dart';
import 'package:intl/date_symbol_data_local.dart';
import 'package:hive_flutter/hive_flutter.dart';
import 'package:path_provider/path_provider.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final document = await getApplicationDocumentsDirectory();
  await initializeDateFormatting();
  await Hive.initFlutter(document.path);
  // Adapter 등록하기
  Hive.registerAdapter<Schedule>(ScheduleAdapter());
  await Hive.initFlutter(document.path);
  runApp(
    const MaterialApp(
      home: TableCalendar(),
    ),
  );
}
