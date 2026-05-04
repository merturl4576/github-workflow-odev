from calc import add, sub, multiply


  def test_add():
      assert add(2, 3) == 5
      assert add(-1, 1) == 0


  def test_sub():
      assert sub(5, 2) == 3
      assert sub(0, 4) == -4


  def test_multiply():
      assert multiply(3, 4) == 12
      assert multiply(5, 0) == 0
