class Validator {
  static String? time(String? val) {
    if (val == null) {
      return '값을 입력해주세요';
    }

    int? number;

    try {
      number = int.parse(val);
    } catch (e) {
      return '숫자를 입력해주세요';
    }

    if (number < 0 || number > 24) {
      return '0시부터 24시 사이를 입력해주세요';
    }

    return null;
  } // 시간값 검증

  static String? content(String? val) {
    if (val == null || val.length == 0) {
      return '값을 입력해주세요';
    }

    return null;
  } // 내용값 검증
}
