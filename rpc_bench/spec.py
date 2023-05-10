from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import toolcli

    # class Call(typing.TypedDict):
    #     jsonrpc: typing.Literal['2.0']
    #     method: str
    #     params: typing.Sequence[typing.Any]
    #     id: int
    Call = typing.Mapping[str, typing.Any]

    MethodCalls = typing.Mapping[str, typing.Sequence[typing.Any]]

    class Node(typing.TypedDict):
        name: str
        url: str
        remote: str | None

    NodesShorthand = typing.Union[
        typing.Sequence[str],
        typing.Sequence[Node],
        typing.Mapping[str, str],
        typing.Mapping[str, Node],
    ]

    NodeMethodLatencies = typing.Mapping[str, typing.Sequence[float]]
    NodesMethodLatencies = typing.Mapping[str, NodeMethodLatencies]

    class LatencyBenchmarkResults(typing.TypedDict):
        nodes: typing.Mapping[str, Node]
        methods: typing.Sequence[str]
        samples: int | None
        calls: typing.Mapping[str, typing.Sequence[str]]
        latencies: NodesMethodLatencies

    class ProgressBar(typing.TypedDict):
        desc: str
        position: int | None
        leave: bool
        colour: str
        disable: bool

    class Test(typing.TypedDict):
        url: str
        rates: typing.Sequence[int]
        duration: int
        calls: typing.Sequence[typing.Any]

    class RawVegetaTestOutput(typing.TypedDict):
        latencies: typing.Mapping[str, float]
        bytes_in: typing.Mapping[str, int]
        bytes_out: typing.Mapping[str, int]
        earliest: str
        latest: str
        end: str
        duration: int
        wait: int
        requests: int
        rate: float
        throughput: float
        success: int
        status_codes: typing.Mapping[str, int]
        errors: typing.Sequence[str]

    class VegetaTestOutput(typing.TypedDict):
        target_rate: int
        actual_rate: float
        target_duration: int
        actual_duration: float
        requests: int
        throughput: float
        success: float
        min: float
        mean: float
        p50: float
        p90: float
        p95: float
        p99: float
        max: float

    class VegetaTestsOutput(typing.TypedDict):
        target_rate: typing.Sequence[int]
        actual_rate: typing.Sequence[float]
        target_duration: typing.Sequence[int]
        actual_duration: typing.Sequence[float]
        requests: typing.Sequence[int]
        throughput: typing.Sequence[float]
        success: typing.Sequence[float]
        min: typing.Sequence[float]
        mean: typing.Sequence[float]
        p50: typing.Sequence[float]
        p90: typing.Sequence[float]
        p95: typing.Sequence[float]
        p99: typing.Sequence[float]
        max: typing.Sequence[float]

    LoadTestOutput = VegetaTestsOutput



styles: toolcli.StyleTheme = {
    'title': 'bold #00e100',
    'metavar': 'bold #e5e9f0',
    'description': '#aaaaaa',
    'content': '#00B400',
    'option': 'bold #e5e9f0',
    'comment': '#888888',
}

