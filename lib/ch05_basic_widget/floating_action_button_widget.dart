import 'package:flutterproject/ch05_basic_widget/column_widget.dart';
import 'package:flutterproject/ch05_basic_widget/expanded_widget.dart';
import 'package:flutterproject/ch05_basic_widget/gesture_detector_widget.dart';
import 'package:flutterproject/ch05_basic_widget/icon_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/outlined_button_widget.dart';
import 'package:flutterproject/ch05_basic_widget/padding_widget.dart';
import 'package:flutterproject/ch05_basic_widget/row_widget.dart';
import 'package:flutter/material.dart';

class FloatingActionButtonExample extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        floatingActionButton: FloatingActionButton(
          // 클릭했을 때 실행할 함수
          onPressed: () {},
          child: Text('클릭'),
        ),
        body: Container(),
      ),
    );
  }
}
