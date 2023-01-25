import 'package:flutterproject/ch05_basic_widgets/column_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/expanded_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/gesture_detector_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/icon_button_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/outlined_button_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/padding_widget.dart';
import 'package:flutterproject/ch05_basic_widgets/row_widget.dart';
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
