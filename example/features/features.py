from xuperchain.context import Context
from xuperchain.driver import Driver
from xuperchain.contract_method import contract_method
from xuperchain.response import Response


class Features():

    @contract_method
    def initialize(self, ctx: Context):
        return Response.ok("ok")

    @contract_method
    def Log(self, ctx: Context):
        ctx.Log("test log")
        return Response.ok("ok")

    @contract_method
    def QueryTx(self, ctx: Context):
        txid = ctx.Args().get("txid")
        if txid is None:
            return Response.error("missing txid")
        resp = ctx.QueryTx(txid=txid)
        return Response.ok(resp.blockid)

    @contract_method
    def QueryBlock(self, ctx: Context):
        blockid = ctx.Args().get("blockid")
        if blockid is None:
            return Response.error("missing blockid")
        block = ctx.QueryBlock(blockid=blockid)
        return Response.ok(block.pre_hash)

    @contract_method
    def Version(self, ctx: Context):
        # modify this value and upgrade contract for upgradable validate
        return Response.ok("v1")


if __name__ == "__main__":
    Driver().serve(Features())
