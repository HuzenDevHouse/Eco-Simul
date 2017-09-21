# -*- coding: utf-8 -*-
# /usr/local/bin/python3

import unittest
import simvector as sv
import numpy as np

class TestVertors(unittest.TestCase):

    # 1. 시뮬레이션을 할 객체벡터가 10,000 개 이상 2상이 있는가?
    # 2. 시뮬레이션 형태가 같은 객체벡터를 비교하는 경우 각 1상의 벡터집합은 같은가?
    # 3. 객체벡터는 속성값을 할당할 만큼 큰가?
    # Make 2 more object vector sets which contains 10,000 vectors.
    # If the simulation type is comparing two equal sets, these should be equal sets.
    # And, each object vector sets have enough dimention to assign the attribute

    def testSimvertorsCreatedRight(self):
        self.assertGreaterEqual(sv.simulacrum.ndim, 2)

    # 속성값에 맞추어서 이를 조정할 수 있는 가중치 행렬이 나온다.
    # 가중치 행렬이 속성값을 다룰 수 있는 크기 인가
    # 가중치가 Overfitting 또는 Underfitting 을 일으키지는 않는가?
    # It Claims 1: 가중치 행렬 W의 원소가 w(i,j) 가 0 <= w <= 1 사이의 값을 가진다
    # It Claims 2: 가중치 행렬이 Feedback 수치 delta_x를 받는다
    # It Claims 3: 반복하여 얻어진 가중치 행렬 W_iter(z) 의 원소가 0 < w < 1의 값을 가진다

    def testWightMatrix(self):
        pass

    # 테스트의 문제점: 뻔한 결과가 나온다. 소득대로 세금을 많이 매기면 많이 낼 수 밖에 없어 지니계수가 1에 수렴한다
    # 문제점의 문제점: 복잡한 사고를 하려고 하면 모델링 자체가 안된다. 이점을 명시 시켜야 한다.
    # 해결의 실마리: 우리의 한계를 주지시킨다. 컴퓨터는 단순히 계산을 빨리하는 것 외에는 없다.
    # 깊게 생각해보기: 모델링을 보다 현실적으로 할 수 있는 방법은 뭐가 있을까?
    # 깊게 생각해보기: 일단 라이버러리를 제작해놓고 이게 뭔진 모르겠지만 쓰게 하고, 궁금한 사람만 보게하자.
