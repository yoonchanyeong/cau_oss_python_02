import math # math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기
class Line:
    """
    Line 클래스는 선의 길이를 나타내는 클래스입니다.
    """
    def __init__(self, length = 1): 
        """Line 객체를 초기화하고 길이를 설정합니다.
        Args:
            length (int or float): 선의 길이 
            초기 생성시 0이하의 값 또는 int/float외의 타입을 전달 받으면, 기본 값=1 입니다.
        """
        if isinstance(length, (int, float)) and length >0:
            self.__length = length
        else:
            self.__length = 1
    
    def set_length(self, length): 
        """선의 길이를 설정합니다.
        Args:
            length (int or float): 설정할 길이
            이후 변경시 0이하의 값 또는 int/float을 전달받으면, 이전 값 입니다.
        """
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
    
    def get_length(self):
        """현재 선의 길이를 반환합니다.
        Returns:
            int or float: 현재 선의 길이
        """
        return self.__length
    
def area_square(line):
    """ 길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    Args:
        line(Line): 정사각형의 한변의 길이입니다.
    returns:
        int or float: 정사각형의 넓이를 반환합니다.
        매개변수의 타입이 Line클래스가 아닌 경우, 숫자 0을 반환합니다.
    """
    if not isinstance(line, Line):
        return 0
    return line.get_length()**2

def area_circle(line):
    """ 길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args:
        line(Line): 반지름의 길이입니다.
    returns:
        int or float: 원의 넓이를 반환합니다.
        매개변수의 타입이 Line클래스가 아닌 경우, 숫자 0을 반환합니다.
    """
    if not isinstance(line, Line):
        return 0
    return line.get_length()**2*math.pi

def area_regular_triangle(line):
    """ 길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    Args:
        line(Line): 정삼각형의 한변의 길이입니다.
    returns:
        int or float: 정삼각형의 넓이를 반환합니다.
        매개변수의 타입이 Line클래스가 아닌 경우, 숫자 0을 반환합니다.
    """
    if not isinstance(line, Line):
        return 0
    return line.get_length()**2*math.sqrt(3)/4

    