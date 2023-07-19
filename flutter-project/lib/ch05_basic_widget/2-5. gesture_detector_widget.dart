import 'package:flutter/material.dart';

void main(){
  runApp(const GestureDetectorWidgetExample());
}

class GestureDetectorWidgetExample extends StatelessWidget {
  const GestureDetectorWidgetExample({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: GestureDetector(
            // 한 번 탭했을 때 실행할 함수
            onTap: () {
              print('on tap');
            },
            // 두 번 탭했을 때 실행할 함수
            onDoubleTap: () {
              print('on double tap');
            },
            // 길게 눌렀을 때 실행할 함수
            onLongPress: () {
              print('on long press');
            },
            // Gesture를 적용할 위젯
            child: Container(
              decoration: const BoxDecoration(
                color: Colors.red,
              ),
              width: 100.0,
              height: 100.0,
            ),
          ),
        ),
      ),
    );
  }
}
