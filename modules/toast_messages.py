# from windows_toasts import ToastDisplayImage, ToastImageAndText4, WindowsToaster
import desktop_notify.aio
import asyncio

from modules.functions import resource_path

# show toast notification
def show_toast(message):
    notify = desktop_notify.aio.Notify("Linux-Toasts", message, resource_path("toast_logo.png"))
    asyncio.run(notify.show())
    # toaster = DesktopNotifier("Windows-Toasts")
    # new_toast = ToastImageAndText4()
    # new_toast.SetBody(message)
    # Hier kannst du den Pfad zu deinem eigenen Bild angeben
    # new_toast.AddImage(ToastDisplayImage.fromPath(resource_path("toast_logo.png")))
    # toaster.show_toast(new_toast)

#def show_toast(message,)