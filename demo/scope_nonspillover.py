from dataclasses import dataclass, field

@dataclass
class DecisionContainer:
    approvals: set[str] = field(default_factory=set)

    def approve(self, decision_id: str) -> None:
        self.approvals.add(decision_id)

    def is_approved(self, decision_id: str) -> bool:
        return decision_id in self.approvals


def scoped_nonspillover() -> bool:
    a = DecisionContainer()
    b = DecisionContainer()
    decision = "same-call-id"
    a.approve(decision)
    return a.is_approved(decision) and not b.is_approved(decision)


def broken_shared_store() -> bool:
    shared=set()
    a=DecisionContainer(shared)
    b=DecisionContainer(shared)
    decision="same-call-id"
    a.approve(decision)
    return a.is_approved(decision) and not b.is_approved(decision)

if __name__ == '__main__':
    print('safe scoped-container relation:', 'PASS' if scoped_nonspillover() else 'FAIL')
    print('deliberately broken shared-store control:', 'DETECTED' if not broken_shared_store() else 'MISSED')
