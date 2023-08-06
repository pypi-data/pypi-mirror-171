$('#modalCharts').html(`<div class="modal-content"><header class="modal-header"><span class="close">×</span><span class="chartimg" id="lastChart">恢复原始</span></header><div class="modal-body">
       <div class="chartcol"><img class="chartimg" id="barChart" src="/static/smartchart/editor/echart/img/bar.webp"></div>
      <div class="chartcol"><img class="chartimg" id="lineChart" src="/static/smartchart/editor/echart/img/line.webp"></div>
      <div class="chartcol"><img class="chartimg" id="pieChart" src="/static/smartchart/editor/echart/img/pie.webp"></div>
      <div class="chartcol"><img class="chartimg" id="gaugeChart" src="/static/smartchart/editor/echart/img/gauge.webp"></div>
      <div class="chartcol"><img class="chartimg" id="diyChart" src="/static/smartchart/editor/echart/img/diy.webp"></div>
      <div class="chartcol"><img class="chartimg" id="mutiChart" src="/static/smartchart/editor/echart/img/multi.webp"></div>
     <div class="chartcol"><div class="chartimg" id="liMTable">滚动表格</div></div>
     <div class="chartcol"><div class="chartimg" id="swaperTable">连播图</div></div>
     <div class="chartcol"><div class="chartimg" id="filterChart">筛选器</div></div>
     <div class="chartcol"><div class="chartimg" id="h1Chart">大字报</div></div>
     <div class="chartcol"><div class="chartimg" id="funnelChart">漏斗图</div></div>
     <div class="chartcol"><div class="chartimg" id="scatterChart">散点图</div></div>
     <div class="chartcol"><div class="chartimg" id="tableChart">表格</div></div>
     <div class="chartcol"><div class="chartimg" id="vueChart">VUE</div></div>
     <div class="chartcol"><div class="chartimg" id="lineUpChart">lineUp图</div></div>
    </div></div>`);

var barChart = `
let series =[];
let dataset = __dataset__;
for (let i=1;i<dataset[0].length;i++){
    series.push({
        type: 'bar',
        itemStyle: {
            borderRadius: 6,
         },
        emphasis:{
            focus: "data"
        }
        //开启堆叠
        //stack: 'A',
        //areaStyle: {},
      }
    )
}

option__name__= {
    dataset:{source:dataset },
    title: {
        text: "",
        textStyle: {
         fontSize: "2rem",
       },
    },
    legend: {
        show:true,
        textStyle: {
         fontSize: "1rem",
       },
    },
    tooltip: {},
    xAxis: {
        type: 'category',
        axisLabel: {
            textStyle: {
                fontSize:"1rem"
            }
       },
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            textStyle: {
                fontSize:"1rem"
            }
       },
    },
    series: series
};
charts.push(myChart__name__);
`;

var lineChart =`
let series =[];
let dataset = __dataset__;
for (let i=1;i<dataset[0].length;i++){
    series.push({
        type: 'line',
        smooth: true,
        //开启堆叠
        //stack: 'A',
        //areaStyle: {},
      }
    )
}

option__name__= {
    dataset:{source:dataset },
    title: {
        text: "",
        textStyle: {
         fontSize: "2rem",
       },
    },
    legend: {
        show:true,
        textStyle: {
         fontSize: "1rem",
       },
    },
    tooltip: {},
    xAxis: {
        type: 'category',
        axisLabel: {
            textStyle: {
                fontSize:"1rem"
            }
       },
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            textStyle: {
                fontSize:"1rem"
            }
       },
    },
    series: series
};
charts.push(myChart__name__);
`;

var pieChart =`
let dataset = __dataset__; 
let series =[];
for (let i=1;i<dataset.length;i++){
    series.push({
        name: dataset[i][0],
        value: dataset[i][1],
        emphasis:{
            focus: "data"
        }
    })
}

option__name__ = {
    title: {
        text: dataset[0][1],
        left: 'center',
        top: 20,
        textStyle: {
            fontSize: "2rem"
        }
    },
    tooltip : {
        trigger: 'item',
    },
    series : [
        {
            name:dataset[0][1],
            type:'pie',
            radius : ['10%', '55%'],
            center: ['50%', '50%'],
            roseType: 'radius', 
            label: {
                normal: {
                    textStyle: {
                        fontSize: "1rem"
                    }
                }
            },
            itemStyle: {
                normal: {
                     borderRadius: 6
                }
            },
            data: series
        }
    ]
};
charts.push(myChart__name__);
`;

var gaugeChart = `
let dataset=__dataset__;
option__name__={ 
    tooltip : {},
    title:{
        text:''
    },
    series: [
    {
        name: dataset[0][1],
        type: 'gauge',
        min: 0,
        max: dataset[1][2],
        splitNumber: 10,
        axisLabel:{
           fontSize: "0.5rem" 
        },
        axisTick:{
            distance: 2,
            length: "5rem",
            splitNumber: 5
        },
        splitLine:{
            distance: 8,
            length: "5%"
        },
        pointer:{
            //circle,rect,roundRect
            //triangle,diamond,pin,arrow
            icon: '',
            length: '60%',
            width: 6
        },
        detail: {
            formatter:'{value}',
            textStyle:{
                fontSize:"1rem"
            },
        },
        data: [
            {value: dataset[1][1],name:dataset[1][0],
             title:{
                show: true,
                fontSize: "0.6rem"
           }
        }]
    }
    ]                        
 };charts.push(myChart__name__);
`;

var filterChart = `
let dataset=__dataset__;
let table ='<span>标题</span><select  id="id_select__name__">';
table = table + '<option value="" selected>----</option>';
 for(let i=1;i<dataset.length;i++){ 
  table = table + '<option>' + dataset[i][0] + '</option>';
 }
table = table + '</select></div></div>'

dom__name__.innerHTML=table;
`;

var tableChart = `
let dataset=__dataset__;
let table = '<div ><table class="table">';
//头部
table += '<thead ><tr>';
for(let j=0; j<dataset[0].length;j++){
  table = table + "<td>" + dataset[0][j] + "</td>";
};
table += "</tr></thead>";

//表主体
table += "<tbody>";
 for(let i=1;i<dataset.length;i++){
    if(i%2==0){table += "<tr class=''>";}
     else{table += "<tr>"};
    for (j=0; j<dataset[i].length;j++){
       table = table + "<td>" + dataset[i][j] + "</td>";
      };
      table += "</tr>";
 };
 table += "</tbody></table></div>";

dom__name__.innerHTML=table;
`;

var vueChart = `
vapp.d__name__ = __dataset__;
`;

var diyChart = `
let dataset = __dataset__; 
let legend_label = ds_rowname(dataset);
let xlabel = dataset[0].slice(1);
dataset = ds_createMap(dataset);

option__name__  = {
   title: {
       text: '',
        left: 'center'
    }, 
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b} : {c}' 
    },
    legend: {
       left: 'center',
       data: legend_label
    }, 
    xAxis: {
        type: 'category',
       data: xlabel
    }, 
    //多Y轴
    yAxis: [{
        type: 'value',
        name:'AAA',
        position:'left',
        axisLabel:{
         formatter:function (value, index) {
            return value/10000 + '万';
    }}
    },{
        type: 'value',
        name:'差异',
        position : 'right',
        
    }],
    
   series: [{
        name: legend_label[0],
        data: dataset[legend_label[0]],
        type: 'bar'
   },
   {
        name: legend_label[1],
       data: dataset[legend_label[1]],
        type: 'bar'
   },{
        name: legend_label[2],
        data: dataset[legend_label[2]],
        type: 'line',
        yAxisIndex:1,
        label:{
            show:true,
            formatter:function(param) {
                if (param.value==0) {return '';} else
                {return param.value;}
        }
    }}
 ]
};
charts.push(myChart__name__);`;

var h1Chart="let dataset = __dataset__;" + '\n' +"let table = `<h1>${dataset[0][0]}</h1><h3>${dataset[1][0]}</h3>`;"+ '\n' + "dom__name__.innerHTML=table;";

var mutiChart = `
let dataset = __dataset__; 
let legend_label = ds_rowname(dataset);
let xlabel = dataset[0].slice(1);
dataset = ds_createMap(dataset);

option__name__= {
  title: [
    {
      left: '20%',
      text: legend_label[0]
    },
    {
      right: '25%',
      text: legend_label[1]
    },
    {
      left: '20%',
      bottom: '50%',
      text: legend_label[2]
    },
    {
      right: '25%',
      bottom: '50%',
      text: legend_label[3]
    }
  ],
  tooltip: {
    trigger: 'axis'
  },
  xAxis: [
    {
      data: xlabel
    },
    {
      data: xlabel,
      gridIndex: 1
    },
    {
      data: xlabel,
      gridIndex: 2
    },
    {
      data: xlabel,
      gridIndex: 3
    }
  ],
  yAxis: [
    {},
    {
      gridIndex: 1
    },
    {
      gridIndex: 2
    },
    {
      gridIndex: 3
    }
  ],
  grid: [
    {
      bottom: '60%',
      right: '55%'
    },
    {
      bottom: '60%',
      left: '55%'
    },
    {
      top: '60%',
      right: '55%'
    },
    {
      top: '60%',
      left: '55%'
    },
  ],
  series: [
    {
      type: 'line',
      showSymbol: false,
      data: dataset[legend_label[0]]
    },
    {
      type: 'bar',
      showSymbol: false,
      data: dataset[legend_label[2]],
      xAxisIndex: 1,
      yAxisIndex: 1
    },
    {
      type: 'bar',
      showSymbol: false,
      data: dataset[legend_label[3]],
      xAxisIndex: 2,
      yAxisIndex: 2
    },
    {
      type: 'line',
      showSymbol: false,
      data: dataset[legend_label[3]],
      xAxisIndex: 3,
      yAxisIndex: 3
    }
  ]
};
charts.push(myChart__name__);
`;

var liMTable= `let dataset = __dataset__; 
let tablebody = '';
let tablehead = '';
for(let i=1; i<dataset.length; i++){
    let item = dataset[i];
    let temp='';
    for(let j=0; j<item.length; j++){
        temp = temp + '<span>' + item[j] + '</span>';
    }
    tablebody =  tablebody +'<li>' + temp + '</li>';
}

for(i=0; i<dataset[0].length; i++){
    tablehead = tablehead + '<span>' + dataset[0][i] + '</span>';
}

let table =` + '`<div class="smtlisthead">${tablehead} </div> <div class="smtlistnav smtlist__name__"> <ul>${tablebody}</ul></div>`;' +
`
dom__name__.innerHTML=table;

ds_liMarquee('.smtlist__name__');
`;

var swaperTable = `
let dataset = __dataset__;
let myslides='';

for(i=1;i<dataset.length;i++){
    myslides = \`\$\{myslides\}<div class="swiper-slide"><img src ="\$\{dataset[i][0]\}"></div>\`;
}

let table = \`<div class="swiper swiper__name__" style="height:100%">
<div class="swiper-wrapper">\$\{myslides\}</div></div>\`;
dom__name__.innerHTML=table;

ds_swiper('.swiper__name__');
`;

var lineUpChart = `
ds_loadcss('smt_LineUp');
ds_loadjs('smt_LineUp');
let dataset = __dataset__;
dataset = ds_createMap_all(dataset);
try{Ljs__name__.destroy()}catch{}
Ljs__name__ = LineUpJS.asLineUp(dom__name__, dataset);
`;
var funnelChart = `
let dataset = __dataset__;
let legend_label = ds_rowname(dataset);
let series =[];
for (let i=1;i<dataset.length;i++){
    series.push({name: dataset[i][0],value: dataset[i][1]})
}

option__name__={
    tooltip: {
        trigger: 'item',
        formatter: "{c}"
    },
    calculable: true,
    series: [
        {
            type:'funnel',
            left: '10%',
            top: 60,
            bottom: 60,
            width: '80%',
            min: 0,
            max: 100,
            minSize: '0%',
            maxSize: '100%',
            sort: 'descending',
            gap: 2,
            label: {
                show: true,
                position: 'inside'
            },
            labelLine: {
                length: 10,
                lineStyle: {
                    width: 1,
                    type: 'solid'
                }
            },
            itemStyle: {
                borderColor: '#fff',
                borderWidth: 1
            },
            emphasis: {
                label: {
                    fontSize: 20
                }
            },
            data: series
        }
    ]                                    
};charts.push(myChart__name__);
`;

var scatterChart=`
let dataset=__dataset__;
dataset=[['x','y'],[10,12],[11,15],[20,31]];
option__name__ = {
    title: {
        text:dataset[0][0]
    },
    xAxis: {},
    yAxis: {},
    series: [{
        symbolSize: 20,
        data: dataset ,
        type: 'scatter'
    }]
};
charts.push(myChart__name__);  
`;