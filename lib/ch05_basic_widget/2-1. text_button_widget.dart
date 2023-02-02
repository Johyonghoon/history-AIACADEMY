import 'package:flutter/material.dart';

class TextButtonWidgetExample extends StatelessWidget {
  const TextButtonWidgetExample({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: TextButton(
            // 클릭 시 실행
            onPressed: () {},
            // 스타일 지정
            style: TextButton.styleFrom(
              // 주 색상 지정
              foregroundColor: Colors.red,
            ),
            // 버튼에 넣을 위젯
            child: const Text('Text Button'),
          ),
        ),
      ),
    );
  }
}
