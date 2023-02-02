import 'package:flutter/material.dart';

void main() {
  runApp(const FloatingActionButtonExample());
}

class FloatingActionButtonExample extends StatelessWidget {
  const FloatingActionButtonExample({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        floatingActionButton: FloatingActionButton(
          // 클릭했을 때 실행할 함수
          onPressed: () {},
          child: const Text('클릭'),
        ),
        body: Container(),
      ),
    );
  }
}
