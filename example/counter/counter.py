from xuperchain.context import Context
from xuperchain.driver import Driver
from xuperchain.contract_method import contract_method
from xuperchain.response import Response


class Counter():

    @contract_method
    def initialize(self, ctx: Context):
        # TODO default value?
        creator = ctx.Args().get("creator", None)
        if not creator:
            return Response.error()
        ctx.PutObject("name", ctx.Initiator())
        ctx.PutObject("creator", creator)
        return Response(status=200, msg="ok")

    @contract_method
    def Increase(self, ctx: Context):
        key = ctx.Args().get("key")
        try:
            value = str(int(ctx.GetObject(key=key)) + 1)
        except:
            value = "1"

        ctx.PutObject(key, value=value)
        return Response(status=200, body=value)

    @contract_method
    def Get(self, ctx: Context):
        key = ctx.Args().get("key")
        value = ctx.GetObject(key)
        if value is None:
            return Response(status=400, msg="key {} not found".format(key))
        return Response(status=200, body=value)

    @contract_method
    def Delete(self, ctx: Context):
        key = ctx.Args().get("key")
        ctx.DeleteObject(key)
        return Response(status=200, body="")


if __name__ == "__main__":
    Driver().serve(Counter())
