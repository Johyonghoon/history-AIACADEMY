import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class CalculatorButton extends StatelessWidget {
  const CalculatorButton({Key? key, required String text}) : super(key: key);

  String? get text => null;

  String? get numberString => null;

  @override
  Widget build(BuildContext context) {
    return Expanded(child: ButtonTheme(
      height: double.infinity,
      child: OutlinedButton(
        onPressed: () {
          pressButton(text, context);
        },
        child: Text(
          text!,
          style: const TextStyle(
            fontSize: 30.0,
            fontWeight: FontWeight.bold,
            color: Colors.black
          ),
        ),
      ),
    ));
  }
  void pressButton(String? text, BuildContext context){
    String? numberString = Provider.of<CalculatorButton>(context).numberString;
    switch(text){
      case "+": break;
      case "-": break;
      case "*": break;
      case "/": break;
    }
  }
}
