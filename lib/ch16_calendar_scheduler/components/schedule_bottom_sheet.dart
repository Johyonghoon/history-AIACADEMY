import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutterproject/admin/utl/logger.dart';
import 'package:flutterproject/admin/utl/validator.dart';
import 'package:flutterproject/ch16_calendar_scheduler/models/schedule.dart';
import 'package:hive/hive.dart';
import 'package:uuid/uuid.dart';
import '../constants/colors.dart';
import 'custom_text_field.dart';


class ScheduleBottomSheet extends StatefulWidget {

  final DateTime selectedDate;

  const ScheduleBottomSheet({
    required this.selectedDate,
    super.key
  });

  @override
  State<ScheduleBottomSheet> createState() => _ScheduleBottomSheetState();
}

class _ScheduleBottomSheetState extends State<ScheduleBottomSheet> {

  final GlobalKey<FormState> formKey = GlobalKey();

  int startTime = 0; // 시작 시간 저장 변수
  int endTime = 0; // 종료 시간 저장 변수
  String content = "";

  @override
  Widget build(BuildContext context) {
    final bottomInset = MediaQuery.of(context).viewInsets.bottom;
    Logger.showToast("2 ScheduleBottomSheet: ");
    return Form(
      // ➊ 텍스트 필드를 한 번에 관리할 수 있는 폼
      key: formKey, // ➋ Form을 조작할 키값
      child: SafeArea(
        child: Container(
          height: MediaQuery.of(context).size.height / 2 +
              bottomInset, // ➋ 화면 반 높이에 키보드 높이 추가하기
          color: Colors.white,
          child: Padding(
            padding:
            EdgeInsets.only(left: 8, right: 8, top: 8, bottom: bottomInset),
            child: Column(
              // ➋ 시간 관련 텍스트 필드와 내용관련 텍스트 필드 세로로 배치
              children: [
                Row(
                  // ➊ 시작 시간 종료 시간 가로로 배치
                  children: [
                    Expanded(
                      child: CustomTextField(
                        // 시작시간 입력 필드
                        label: '시작 시간',
                        isTime: true,
                        onSaved: (String? val) {
                          // 저장이 실행되면 startTime 변수에 텍스트 필드 값 저장
                          Logger.showToast(" ### startTime ### $val");
                          startTime = int.parse(val!);
                        },
                        validator: Validator.time,
                      ),
                    ),
                    const SizedBox(width: 16.0),
                    Expanded(
                      child: CustomTextField(
                        // 종료시간 입력 필드
                        label: '종료 시간',
                        isTime: true,
                        onSaved: (String? val) {
                          // 저장이 실행되면 endTime 변수에 텍스트 필드 값 저장
                          Logger.showToast(" ### endTime ### $val");
                          endTime = int.parse(val!);
                        },
                        validator: Validator.time,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 8.0),
                Expanded(
                  child: CustomTextField(
                    // 내용 입력 필드
                    label: '내용',
                    isTime: false,
                    onSaved: (String? val) {
                      // 저장이 실행되면 content 변수에 텍스트 필드 값 저장
                      Logger.showToast(" ### content ### $val");
                      content = val!;
                    },
                    validator: Validator.content,
                  ),
                ),
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    // [저장] 버튼
                    // ➌ [저장] 버튼
                    onPressed: onSavePressed,
                    style: ElevatedButton.styleFrom(
                      primary: PRIMARY_COLOR,
                    ),
                    child: Text('저장'),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  void onSavePressed() async {
    Logger.showToast("3 onSavePressed: ");
    formKey.currentState!.save();
    final schedules = Hive.box<Schedule>('schedules');
    String temp = const Uuid().v4();
    Logger.showToast("4 ID: $temp");
    Schedule schedule = Schedule(temp, content!, widget.selectedDate, startTime!, endTime!);
    schedules.put(temp, schedule);
    final Schedule? returnSchedule = schedules.get(temp);
    final String res = returnSchedule.toString();
    Logger.showToast("5 final: $res");
    // Navigator.of(context).pop();

  }

}