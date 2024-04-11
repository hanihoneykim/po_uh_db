window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple, {
            labels: {
                placeholder: "검색...", // 검색 입력란의 플레이스홀더
                perPage: "페이지 당 항목", // 페이지 당 항목 드롭다운 레이블
                noRows: "데이터가 없습니다.", // 레코드가 없을 때 표시되는 메시지
                info: "총 _TOTAL_ 항목 중 _START_ - _END_ 표시", // 페이지 정보 텍스트
                infoFiltered: "(_MAX_ 항목의 필터링 결과로부터 필터링 됨)", // 필터링된 결과 텍스트
            }
        });
    }
});
