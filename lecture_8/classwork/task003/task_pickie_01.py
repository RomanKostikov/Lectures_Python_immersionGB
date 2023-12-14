# 3. Pickle
# 🔥 Крайне важно! Модуль pickle не занимается проверкой потока байт на
# безопасность перед распаковкой. Не используйте его с тем набором байт,
# безопасность которого не можете гарантировать.
import os
import pickle

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }')  # print(res)

os.system('echo Hello world!')
# В этом безобидном примере модуль получил доступ к консоли и вывел сообщение
# “Привет, мир!” прежде чем десериализовать поток байт в число ноль.
