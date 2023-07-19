import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutterproject/ch22_calculator/screens/home_screen.dart';
import 'package:provider/provider.dart';

void main(){
  runApp(const App());
}

class App extends StatelessWidget {
  const App({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: ChangeNotifierProvider(
        create: (_) => null,
        child: const HomeScreen(),
      ),
    );
  }
}
