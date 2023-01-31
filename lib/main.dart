import 'package:flutter/material.dart';

void main(){
  runApp(MaterialApp(home: HomeScreen()));
}

class HomeScreen extends StatelessWidget{
  var message = 'Hello Flutter, \n 반갑다 플러터 !! 아주 반가워';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Text(message,
            style: TextStyle(color: Colors.black, fontSize: 50.0),
        ),
      ),
    );
  }
}
