
import 'package:flutter/material.dart';

void main(){
  runApp(MaterialApp(home: HomeScreen()));
}

class HomeScreen extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text('Hello World, \n 반갑다 플러터 !!',
          style: TextStyle(color: Colors.black, fontSize: 50.0),
        ),
      ),
    );
  }
}