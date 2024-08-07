
def remove_key_from_dict(dictionary: dict):
    dictionary.popitem()
def clear_all(dictionary: dict):
    dictionary = { }
a = {'x': 1, 'y': 2}
remove_key_from_dict(a)
print(a)
clear_all(a)
print(a)

####המילון שנשלח לפונקציה הראשונה ישתנה מאחר והמילון הוא mutable
#כלומר מה שישלח לפונקציה הוא פוינטר למיקום המילון בזכרון
#ואילו מה שנשלח לפונקציה השניה לא ינקה את המילון, מאחר ובעקבות פעולה זו נוצר מילון חדש ונקי
#עקרונית אפשר להגדיר את המילון כמשתנה גלובלי, אף על פי שזה לא נהוג ויש להזהר מפעולה כזו. בנוסף
#אפשר גם להחזיר את המילון באמצעות return

