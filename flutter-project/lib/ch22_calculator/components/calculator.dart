import 'package:flutter/material.dart';
import 'package:flutterproject/ch22_calculator/components/calculator_button.dart';

class Calculator extends StatelessWidget {

  late String titleAdd;
  late String titleSub;
  late String titleMul;
  late String titleDiv;

  Calculator({
    required Key key,
    titleAdd,
    titleSub,
    titleMul,
    titleDiv
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(child: Row(
      children: const <Widget>[
        CalculatorButton(text: "+"),
        CalculatorButton(text: "-"),
        CalculatorButton(text: "*"),
        CalculatorButton(text: "/"),
      ],
    ));
  }
}
