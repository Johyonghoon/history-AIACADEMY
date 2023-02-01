import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutterproject/ch23_caculator_37/components/display.dart';
import 'package:flutterproject/ch23_caculator_37/components/keyboard.dart';
import 'package:flutterproject/ch23_caculator_37/providers/calculator_provider.dart';

class Calculator extends StatefulWidget {

  const Calculator({super.key});

  @override
  State<Calculator> createState() => _CalculatorState();
}

class _CalculatorState extends State<Calculator> {

  final CalculatorProvider provider = CalculatorProvider();

  _onPressed(String command){
    setState(() {
      provider.applyCommand(command);
    });
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Column(
        children: [
          Display(text: provider.value,),
          Keyboard(onPressed: _onPressed)
        ],
      ),
    );
  }
}
